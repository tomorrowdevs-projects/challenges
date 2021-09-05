module Vaporcode where

import Data.List (intercalate)
import Data.Char (toUpper)

vaporcode :: String -> String
vaporcode = intercalate "  " . map (pure . toUpper) . concat . words