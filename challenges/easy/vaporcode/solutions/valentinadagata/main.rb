def vaporwave(s)
  s = s.upcase
  s.gsub!(/\s+/, '')
  s = s.chars
  puts s.join(" ")

end

vaporwave("Hello, World!")