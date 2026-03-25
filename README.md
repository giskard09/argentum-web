# ARGENTUM web

Frontend for the ARGENTUM karma economy.

Live: https://giskard09.github.io/argentum-web/

## Views

- **commons** — verified actions feed + pending attestation queue
- **submit** — submit a new action for community verification
- **trace** — look up any entity's wisdom trace
- **leaderboard** — top entities by karma

## Connect to core

The web expects `argentum-core` running at `localhost:8017`.
For production, update the `API` constant in `index.html`.

## Stack

Vanilla HTML/CSS/JS. No framework. Runs as static files.

```bash
python3 -m http.server 8018
```

## License

Apache 2.0
