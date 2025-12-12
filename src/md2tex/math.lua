function Math(el)
    local text = el.text:match("^%s*(.-)%s*$")
    if el.mathtype == 'DisplayMath' then
      return pandoc.RawInline('tex', '\n\\begin{equation}\n' .. text .. '\n\\end{equation}\n')
    elseif el.mathtype == 'InlineMath' then
        return pandoc.RawInline('tex', '$' .. text .. '$')
    else
      return el
    end
  end