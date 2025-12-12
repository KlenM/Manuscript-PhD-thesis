$pdf_mode = 1;
$emulate_aux = 1;
$out_dir = '.';
$aux_dir = '.aux';

@default_files = ('main.tex');
$pdflatex = 'lualatex --shell-escape %O %S';

$bibtex = "biber --input-directory=.aux --output-directory=.aux %B";
$bibtex_use = 2; # 0=never, 1=use bibtex, 2=use bibtex or biber depending on $bibtex