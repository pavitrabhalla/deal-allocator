<p align="center">
  <a href="[https://deal-allocator.vercel.app/](https://deal-allocator.vercel.app/)">
    <h3 align="center">Deal Allocator</h3>
  </a>
</p>

<p align="center">Investment allocator, built with a Python/Flask backend, and a React/Next.js/Typescript frontend</p>

<br/>

## Introduction

This app takes allocation requests from investors and returns prorated investments based on the request, and past average investment activity.

It follows the algorithm rules as described in the prompt. See prompt/README.md


## Demo

[https://deal-allocator-pavitra.vercel.app/](https://deal-allocator-pavitra.vercel.app/)


## Startup script

Install pnpm:
https://pnpm.io/installation (For mac, you can run `brew install pnpm`)

```bash
pnpm dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

The Flask server will be running on [http://127.0.0.1:5328](http://127.0.0.1:5328)

## Tests

This runs the test case examples provided in the prompt, and some additional edge cases
```
pnpm test-api
```

## Code Structure

--api
  --modules
    --prorater.py (This is where the algorithm is)
  --tests
    --index.py (This is where the api tests are)
--app
  --page.tsx (This is the page that renders the home screen)
