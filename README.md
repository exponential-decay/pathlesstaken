# pathlesstaken

Profile strings, e.g. file paths for digital preservation considerations, e.g.
characters that you want to preserve, or characters that you don't want to
preserve.

## Basis for this module

The original analysis was based around this non-recommended filenames from
Microsoft: [Non-recommended names from Microsoft][pathless-1]

[pathless-1]: http://msdn.microsoft.com/en-us/library/aa365247(VS.85).aspx

The code also contains copy Cooper Hewitt's code to enable writing of plain
text descriptions of Unicode characters. This portion of the code is licensed
[BSD 3-Clause "New" or "Revised" License][pathless-3]

* [Py-Unicode at Cooper Hewitt][pathless-2]

[pathless-2]: https://github.com/cooperhewitt/py-cooperhewitt-unicode
[pathless-3]: https://github.com/cooperhewitt/py-cooperhewitt-unicode/blob/master/LICENSE

The bigger project this code was developed for is still here:
[droid-siegfried-sqlite-analysis][pathless-4]

[pathless-4]: https://github.com/exponential-decay/droid-siegfried-sqlite-analysis-engine

## Example output

Given a Unicode string: `❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟`
```bash
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x2764, HEAVY BLACK HEART: ❤'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x1f496, SPARKLING HEART: 💖'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x1f499, BLUE HEART: 💙'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x1f49a, GREEN HEART: 💚'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x1f49b, YELLOW HEART: 💛'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x1f49c, PURPLE HEART: 💜'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x1f49d, HEART WITH RIBBON: 💝'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x2655, WHITE CHESS QUEEN: ♕'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x2656, WHITE CHESS ROOK: ♖'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x2657, WHITE CHESS BISHOP: ♗'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x2658, WHITE CHESS KNIGHT: ♘'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x2659, WHITE CHESS PAWN: ♙'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x265a, BLACK CHESS KING: ♚'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x265b, BLACK CHESS QUEEN: ♛'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x265c, BLACK CHESS ROOK: ♜'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x265d, BLACK CHESS BISHOP: ♝'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x265e, BLACK CHESS KNIGHT: ♞'
File: '❤💖💙💚💛💜💝♕♖♗♘♙♚♛♜♝♞♟' contains, characters outside of ASCII range: '0x265f, BLACK CHESS PAWN: ♟'
```

You can also run a [print test][pathless-5] by running: `$ pathlesstaken.py test`

[pathless-5]: https://twitter.com/paintergoblin/status/916916413419237378

```
File: 'COM4' contains, reserved name 'COM4'
File: 'COM4.txt' contains, reserved name 'COM4'
File: 'AUX' contains, reserved name 'AUX'
File: 'CON' contains, reserved name 'CON'
File: 'space ' has a SPACE as its last character
File: 'period.' has a period '.' as its last character
File: 'ó' contains, characters outside of ASCII range: '0xf3, LATIN SMALL LETTER O WITH ACUTE: ó'
File: 'é' contains, characters outside of ASCII range: '0xe9, LATIN SMALL LETTER E WITH ACUTE: é'
File: 'ö' contains, characters outside of ASCII range: '0xf6, LATIN SMALL LETTER O WITH DIAERESIS: ö'
File: 'óéö' contains, characters outside of ASCII range: '0xf3, LATIN SMALL LETTER O WITH ACUTE: ó'
File: 'óéö' contains, characters outside of ASCII range: '0xe9, LATIN SMALL LETTER E WITH ACUTE: é'
File: 'óéö' contains, characters outside of ASCII range: '0xf6, LATIN SMALL LETTER O WITH DIAERESIS: ö'
File: 'file[bracket]one.txt' contains, non-recommended character: '0x5b, LEFT SQUARE BRACKET: ['
File: 'file[bracket]one.txt' contains, non-recommended character: '0x5d, RIGHT SQUARE BRACKET: ]'
File: 'file[two.txt' contains, non-recommended character: '0x5b, LEFT SQUARE BRACKET: ['
File: 'filethree].txt' contains, non-recommended character: '0x5d, RIGHT SQUARE BRACKET: ]'
File: '-=_|"' contains, non-recommended character: '0x7c, VERTICAL LINE: |'
File: '-=_|"' contains, non-recommended character: '0x22, QUOTATION MARK: "'
File: '(<>:"/\?*|-)' contains, non-recommended character: '0x3c, LESS-THAN SIGN: <'
File: '(<>:"/\?*|-)' contains, non-recommended character: '0x3e, GREATER-THAN SIGN: >'
File: '(<>:"/\?*|-)' contains, non-recommended character: '0x3a, COLON: :'
File: '(<>:"/\?*|-)' contains, non-recommended character: '0x22, QUOTATION MARK: "'
File: '(<>:"/\?*|-)' contains, non-recommended character: '0x2f, SOLIDUS: /'
File: '(<>:"/\?*|-)' contains, non-recommended character: '0x5c, REVERSE SOLIDUS: \'
File: '(<>:"/\?*|-)' contains, non-recommended character: '0x3f, QUESTION MARK: ?'
File: '(<>:"/\?*|-)' contains, non-recommended character: '0x2a, ASTERISK: *'
File: '(<>:"/\?*|-)' contains, non-recommended character: '0x7c, VERTICAL LINE: |'
File: '(<>:"/\?*|-)' contains, non-printable character: '0x0, <control character>'
File: '(<>:"/\?*|-)' contains, non-printable character: '0x1f, <control character>'
```

Please let me know how it goes if you try out this code.

## Sister project

If you like to understand your filepaths, but don't need all the detail,
there's a third-way, by taking a look at the [fndec][pathless-6] project I
created in Golang and using utilities from Richard Lehane's
[Siegfied][pathless-7]. More info after the jump.

[pathless-6]: https://github.com/exponential-decay/fndec
[pathless-7]: https://github.com/richardlehane/siegfried

### License

This unique parts of this code is licensed using [GPLv3](LICENSE)
