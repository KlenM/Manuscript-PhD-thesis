import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    import subprocess
    import tempfile
    import json
    import regex as re
    return Path, json, re, subprocess, tempfile


@app.cell
def _(Path):
    MD_PATH = Path("../../content/").resolve()
    TEX_PATH = Path("../tex/converted/").resolve().absolute()
    return MD_PATH, TEX_PATH


@app.cell
def _(subprocess):
    def md_to_tex(input_path: str, output_path: str) -> None:
        cmd = [
            "pandoc",
            "-f", "markdown+lists_without_preceding_blankline",
            input_path,
            # "--filter", "pandoc-crossref",
            "--lua-filter", "math.lua",
            "--lua-filter", "filters.lua",
            "-o", output_path,
        ]
        subprocess.run(cmd, check=True)
    return (md_to_tex,)


@app.cell
def _(re):
    def preprocess_md(md_content):
        md_content = re.sub(r'<span[^>]*>.*?</span>', '', md_content, flags=re.DOTALL) # Lineage html tag to delete
        md_content = re.sub(r' ?\^\[@([^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)+)\]', r' \\cite{zot??}', md_content) # zotero ref
        md_content = re.sub(r' ?\^\[@(.+?)\]', r' \\cite{\1}', md_content) # new cite style
        md_content = re.sub(r' ?\^\[((?:sec|eq|fig|tab):.+?)\]', r' \\cref{\1}', md_content) # new ref style
        # md_content = re.sub(r"\^\[@[^\[\]]*(?:\[[^\[\]]*\][^\[\]]*)*\]", r'', md_content) # delete my notes
        # md_content = re.sub(r'@([\w_\?\:]+)', r'\\autoref{\1}', md_content) # old ref style

        md_content = md_content\
            .replace('file:///home/klen/syncthing/desktop/physics/phd/thesis/images/', '')\
            .replace('file:///home/klen/syncthing/desktop/physics/phd/thesis/src/generated/', '')\
            .replace(r'%\label', r'\label')\

        return md_content

    def postprocess_tex(tex_content):
        tex_content = re.sub(r'(\\begin\{align\})\n+', r'\1\n', tex_content)
        tex_content = re.sub(r'\n+(\\end\{align\})', r'\n\1', tex_content)

        tex_content = tex_content\
            .replace(r'\pandocbounded', '')\
            .replace(r'\tightlist', '')\
            .replace(r'\includesvg[keepaspectratio]', r'\includesvg[inkscapelatex=false,keepaspectratio]')\
            .replace(r'longtable', r'tabular')\
            .replace(r'\endhead', '')\
            .replace(r'\endlastfoot', '')\

        return tex_content
    return postprocess_tex, preprocess_md


@app.cell
def _(MD_PATH, TEX_PATH, md_to_tex, postprocess_tex, preprocess_md, tempfile):
    def run_conversion():
        for md_path in MD_PATH.rglob('*.md'):
            tex_path = TEX_PATH / md_path.relative_to(MD_PATH).with_suffix('.tex')
            tex_path.parent.mkdir(parents=True, exist_ok=True)

            with open(md_path, 'r', encoding='utf-8') as f:
                md_content = f.read()

            with tempfile.NamedTemporaryFile(suffix=".md", delete_on_close=False, mode='w', encoding='utf-8') as tmp_md:
                tmp_md.write(preprocess_md(md_content))
                tmp_md.close()
                md_to_tex(tmp_md.name, str(tex_path))

            with open(tex_path, 'r', encoding='utf-8') as f:
                tex_content = f.read()

            with open(tex_path, 'w', encoding='utf-8') as f:
                f.write(postprocess_tex(tex_content))

    run_conversion()
    return


@app.cell(disabled=True)
def _(MD_PATH, json, subprocess):
    def show_key_structure(d, indent=0, skip_keys=None):
        prefix = "  " * indent
        skip_keys = skip_keys  if skip_keys is not None else  []
        if isinstance(d, dict):
            for k, v in d.items():
                if k.strip() in skip_keys:
                    continue
                vtype = type(v).__name__
                print(f"{prefix}{k}/ ({vtype})")
                show_key_structure(v, indent + 1, skip_keys=skip_keys)
        elif isinstance(d, list):
            print(f"{prefix}- [List]")
            for i, v in enumerate(d[:1]):  # show just first item for structure
                show_key_structure(v, indent + 1, skip_keys=skip_keys)


    def pandoc_inspect(input_path: str) -> dict:
        cmd = [
            "pandoc",
            "-f", "markdown+lists_without_preceding_blankline",
            input_path,
            "--lua-filter", "math.lua",
            "--lua-filter", "filters.lua",
            "-t", "json"
        ]
        res = subprocess.run(cmd, check=True, capture_output=True, text=True)
        return json.loads(res.stdout)

    file_ast = pandoc_inspect(MD_PATH / "2_background/2_2_rand_func.md")
    show_key_structure(file_ast)
    return (file_ast,)


@app.cell
def _(file_ast):
    [b['t'] for b in file_ast['blocks']]
    return


@app.cell
def _(file_ast):
    file_ast['blocks'][3]['c']
    return


if __name__ == "__main__":
    app.run()
