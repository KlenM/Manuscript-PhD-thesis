-- function Figure(el)
--   -- If the paragraph contains a single image (possibly with caption)
--   --return el
--   local attr, caption_inlines, target = unpack(el.c)
--   local src, title = unpack(target)
--   return string.format("\\addimghere{%s}{0.8}{%s}{}", src, caption_text)
--   -- return pandoc.RawBlock('latex', '\\addimagehere{}')
-- end

function BlockQuote(block)
  return {}
end