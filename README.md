## mathing

Practice math with a clean MVC architecture.

### Run

```
uv run python -m mathing.main
```

### Architecture (MVC)

- Models: `app/models` (Peewee models and simple data objects)
- Views: `app/views` (Console or TUI UI layers)
- Controllers: `app/controllers` (application orchestration)
- Services: `app/services` (business logic: question generation, timing)

Legacy modules remain as thin shims with deprecation notes.
