# Input schema

The Word renderer accepts UTF-8 JSON with this structure:

```json
{
  "title": "项目实践与能力成长记录",
  "period_summary": {
    "项目概述": "Optional summary text",
    "阶段成果": ["Optional bullet"]
  },
  "entries": [
    {
      "date": "2026-08-18",
      "project": "Example project",
      "stage": "Implementation",
      "sections": {
        "当日目标": ["One goal"],
        "我完成的工作": ["One supported action"],
        "AI辅助与团队协作": ["One accurately attributed action"],
        "使用的知识、技巧、方法与策略": ["One applied method"],
        "关键决策及依据": ["Decision and rationale"],
        "项目推进与可验证结果": ["Result and evidence"],
        "遇到的问题及解决方式": ["Problem and resolution"],
        "体现的能力": ["Evidence-based capability"],
        "下一步计划": ["Next action"]
      }
    }
  ]
}
```

Rules:

- `title` is optional and defaults to `项目实践与能力成长记录`.
- `period_summary` is optional. Values may be strings or arrays of strings.
- `entries` is required and must be a non-empty array.
- Each entry requires ISO date `YYYY-MM-DD`, project name, and non-empty `sections`.
- `stage` is optional.
- Section values may be strings or arrays of strings.
- Empty values are omitted from the Word document.
- The renderer does not infer or verify facts. Evidence validation belongs to the agent workflow.

