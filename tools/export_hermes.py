"""Export the bgb Claude Code plugin as Hermes Agent (Nous Research) skills.

Hermes Agent consumes the same agentskills.io SKILL.md standard, but flat
(no plugin namespace) and without Claude Code's runtime conveniences. This
script converts bgb/skills/* into hermes/skills/bgb-* :

- folder + `name:` renamed help -> bgb-help (etc.) to avoid collisions
- `${CLAUDE_PLUGIN_ROOT}/references/...` -> skill-local `references/...`
  (the shared reference files are copied into every skill folder)
- `/bgb:xxx` invocations -> `/bgb-xxx`
- Claude-only frontmatter (disable-model-invocation, argument-hint,
  allowed-tools) dropped; name/version/metadata.hermes added
- a fallback note for `$ARGUMENTS` substitution

Re-run after editing any source skill:  python tools/export_hermes.py
"""

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "bgb"
OUT = ROOT / "hermes" / "skills"

ARGS_NOTE = (
    "> **Arguments:** the text the user typed after the slash command. "
    "If `$ARGUMENTS` below shows literally (not substituted), read the "
    "arguments from the user's invocation message instead.\n"
)


def transform_body(text: str) -> str:
    text = text.replace("${CLAUDE_PLUGIN_ROOT}/references/", "references/")
    text = text.replace("${CLAUDE_PLUGIN_ROOT}", "this skill's directory")
    text = re.sub(r"/bgb:(\w+)", r"/bgb-\1", text)
    return text


def parse_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        raise ValueError("no frontmatter")
    fm, body = m.group(1), m.group(2)
    desc = re.search(r"^description:\s*(.+)$", fm, re.MULTILINE)
    return (desc.group(1).strip() if desc else ""), body


def main():
    version = json.loads(
        (SRC / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8")
    )["version"]

    if OUT.parent.exists():
        shutil.rmtree(OUT.parent)
    OUT.mkdir(parents=True)

    refs = sorted((SRC / "references").glob("*.md"))
    skills = sorted(p for p in (SRC / "skills").iterdir() if p.is_dir())

    for skill_dir in skills:
        name = f"bgb-{skill_dir.name}"
        dest = OUT / name
        dest.mkdir()

        desc, body = parse_frontmatter(
            (skill_dir / "SKILL.md").read_text(encoding="utf-8")
        )
        desc = transform_body(desc)
        body = transform_body(body)

        # insert the $ARGUMENTS fallback note right after the H1 title
        if "$ARGUMENTS" in body:
            body = re.sub(r"^(# .+\n)", r"\1\n" + ARGS_NOTE, body, count=1,
                          flags=re.MULTILINE)

        fm_lines = [
            "---",
            f"name: {name}",
            f"description: {desc}",
            f"version: {version}",
            "metadata:",
            "  hermes:",
            "    tags: [board-games, tabletop, strategy]",
            "    category: games",
            "---",
            "",
        ]
        (dest / "SKILL.md").write_text(
            "\n".join(fm_lines) + body, encoding="utf-8", newline="\n"
        )

        ref_dest = dest / "references"
        ref_dest.mkdir()
        for ref in refs:
            content = transform_body(ref.read_text(encoding="utf-8"))
            (ref_dest / ref.name).write_text(content, encoding="utf-8",
                                             newline="\n")
        print(f"  {name}  (SKILL.md + {len(refs)} reference files)")

    print(f"\nExported {len(skills)} skills (v{version}) -> {OUT}")


if __name__ == "__main__":
    main()
