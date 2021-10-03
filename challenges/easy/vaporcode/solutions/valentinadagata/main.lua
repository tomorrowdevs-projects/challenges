function vaporwave(s)
  s = s:gsub("%s+", "")
  s = s:upper()
  s = s:gsub('(.)','%1 ');
  return s
end

print(vaporwave("Hello,  World!"))