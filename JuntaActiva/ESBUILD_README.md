Esbuild dev/build instructions

Run these in PowerShell from the project root:

1) Install dev dependencies (if not already installed):

```powershell
& 'C:\Program Files\nodejs\npm.cmd' install
```

2) Start esbuild dev server (serves `dist` and rebuilds on change):

```powershell
npx esbuild --bundle client/src/main.tsx --outfile=dist/main.js --servedir=dist --serve=5000 --sourcemap --jsx=automatic
```

3) Build for production:

```powershell
npx esbuild --bundle client/src/main.tsx --outfile=dist/main.js --minify --sourcemap --jsx=automatic
```

4) Serve built files for testing:

```powershell
npx http-server dist -p 5000
```

Note: I also added npm scripts `esbuild:dev`, `esbuild:build`, and `esbuild:serve` to `package.json`.
