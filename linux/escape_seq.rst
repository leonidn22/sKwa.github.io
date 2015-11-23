Escape sequences
================

\x1b[2K     -   clear current line
\x1b[1A     -   move cursor up
\x1b[0G     -   move to start line

Text attributes
0   All attributes off
1   Bold on
4   Underscore (on monochrome display adapter only)
5   Blink on
7   Reverse video on
8   Concealed on 

Foreground colors
30  Black
31  Red
32  Green
33  Yellow
34  Blue
35  Magenta
36  Cyan
37  White

Background colors
40  Black
41  Red
42  Green
43  Yellow
44  Blue
45  Magenta
46  Cyan
47  White

Esc[<line #>;<col #>H
Esc[<line #>;<col #>f
  Cursor Position:
  Moves the cursor to the specified position (coordinates).
  If you do not specify a position, the cursor moves to the home position
  at the upper-left corner of the screen (line 0, column 0). This escape 
  sequence works the same way as the following Cursor Position escape 
  sequence.
