# DevBuddy

This is my Hackclub Terra week 2 project. It's called **DevBuddy**, it runs in your terminal, and it does three things: todo lists, an AI coding assistant (that is quite rightly is BYOK only), and one motivational quote per day.

It's not fancy. It's not polished. But it works on my machine.

## What it actually does

- **`todo`** — A todo list that lives in a JSON file. Add, edit, complete, delete tasks. No sync, no cloud, no accounts. Just you and your growing pile of undone chores.
- **`codex`** — Ask GPT-6-Luna a coding question, get a short answer back (mostly). Your prompt history is saved locally to a JSON file to quit the squaffle with GDPR. There's a "please confirm you'll use this responsibly" step, which I added because I want to, not because typing "confirm" has ever stopped anybody.
- **`give-me-motivation`** — One quote a day. Come back tomorrow for another one. Yes, even that is rate-limited not to stop anyone.

## Usage

```bash
python devbuddy.py [command]
```

The commands are `todo`, `codex`, and `give-me-motivation`. If you've forgotten them, use `--help`:

```bash
python devbuddy.py --help
```

Pro tip: quitting most tools is `q` or `exit`. I'm not above stealing your Ctrl+C, but I haven't got around to it yet.

## Installation

You need Python 3.10+ (the `pyproject.toml` says so, and I see no reason to argue with it).

```bash
git clone https://github.com/Central3465/DevBuddy.git
cd devbuddy
pip install openai python-dotenv winotify
```

If you want the proper grown-up install (a `devbuddy` / `db` command on your PATH):

```bash
pip install .
devbuddy todo
```

## The why for python packages

- **Winotify** is used for Windows toast notifications.
- **python-dotenv** is used to recognise .env files and variables.
- **openai** is used for feeding my goldfish (use your prefrontal cortex).

## Configuration & environment variables

The AI assistant needs one thing to work:

```
OPENAI_API_KEY=sk-your-key-here
```

Put it in a `.env` file in the project root (that's what `python-dotenv` is for) or export it in your shell. Without it, codex will print a sad message and then politely fail.

## Privacy

Everything is stored in JSON files in the `data/` folder (`todo.json`, `chat.json`, `motivation.json`). Nothing goes to any server of mine, because I don't *have* any servers. The only thing leaving your machine is your prompt to OpenAI's API, and only when you use codex. If you don't want that, don't use codex — todo and motivation work perfectly offline.

## Contributing

Sure, go ahead. Check and test your code before you send a PR. One more thing: **no vibe coding.** If you can't explain why your change works, it doesn't (yet).

## Credits

- OpenAI Python API — https://developers.openai.com/api/reference/python
- ZenQuotes - https://zenquotes.io/?ref=public_apis

## License

MIT. Do whatever, I have no plans of developing further after Terra.
