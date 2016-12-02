module Main exposing (..)

import Html exposing (text)

ask : String -> String -> String

ask thing location = 
    "is there a " ++ thing ++ " in your " ++ location

main = 
    text <| ask "fish" "wallet"