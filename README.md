# News Aggregator
https://news-aggregator-blush.vercel.app/

A simple news aggregator app built in Python + Flask. Headlines are scraped using beautifulsoup. Deployed via Vercel.

# Debugging

## Automatically reloading for TailwindCSS
Run the following command to automatically compile and watch changes for Tailwind CSS: </br>
```
npx tailwindcss -i ./static/src/input.css -o ./static/dist/css/output.css --watch
```

## Automatically reloading the Flask app server
To automatically reload the Flask app server for changes in VS Code, you must add the debug configuration using the `launch.json` in `.vscode`. Then, you can debug using the `Python Debugger: Flask`.

The `.vscode` and `launch.json` was manually created.


# Deployment

This app is deployed via Vercel. Some configuration was required.

There must be an `api` directory with the following structure.
```
├── api
│   ├── static
│   ├── templates
│   └── app.py
```

A `vercel.json` must also be created in the project's root directory with the proper `builds` and `routes`.


