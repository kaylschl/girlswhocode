# //insert javascript here
# function toUWU(){
#   var englishInput = document.getElementById('word').value;
#   var uwuOUT = "";
#     for(var i = 0; i < englishInput.length; i++ ){
#       if ((englishInput.charAt(i) == 'r') || (englishInput.charAt(i) == 'l')){
#         uwuOUT = uwuOUT + "w";
#       }
#       else if (englishInput.charAt(i) == 'n'){
#         uwuOUT = uwuOUT + "ny";
#       }
#       else if (englishInput.charAt(i) == '!'){
#         uwuOUT = uwuOUT + "~ uwu";
#       }
#       else{
#         uwuOUT = uwuOUT + englishInput.charAt(i);
#       }
#     }
#     document.getElementById("demo").innerHTML = uwuOUT;
#     console.log(uwuOUT);
# }

secret = "@z/:;=!;_%/#;e*z;$%o#;-#_=-#-;:*;: %!/d%:#;:$=/;]#//%r#;&e;$%!-,;=;%];%--=!r;=!;d*:/;*a; %!-*];?* -/;%!-;/#!:#!_#/;:*;]%b#;:$=/;]* #;-=aa=_zd:n;&d%$;&d%$;&d%$n; */#/;% #; #-,;o=*d#:/;% #;&dz#,;=;d=b#;_$*_*d%:#/;&z:;!*:;:$#;*!#/;a *];e*zn;*b%e;=;:$=!b;=;$%o#;-=/_*z %r#-;%!e;]%!z%d;: %!/d%:=*!n;!*?;a* ;:$#; #%d;]#//%r#p;$#dd*;:#%],;_*!r %:zd%:=*!/;*!;-#_=x$# =!r;:$=/;]#//%r#n;$*?#o# ,;?#;% #;!*:;wz=:#;-*!#;e#:n;e*z;]z/:;r*;*!:*;]=]=_$#!226@r=:$z&n=*;%!-;a=!-;:$#;/#_ #:;]#//%r#n;*!_#;e*z;a=!-;:$#;/#_ #:;]#//%r#,;#!:# ;=:;:*;:$#;_*?;x *]x:"

clues = {
'!': 'n', ' ': 'r', '#': 'e', '%': 'a', '$': 'h', '&': 'b', '*': 'o', '-': 'd', '/': 's', ';': ' ', ':' : 't', '=': 'i', '?': 'w', '@': 'j', ']': 'm', '_': 'c', 'a': 'f', '`': 'x', 'b': 'k', 'e': 'y', 'd': 'l', 'f': '/', 'o': 'v', 'n': '.', 'p': ':', 'r': 'g', 'w': 'q', 'x': 'p', 'z': 'u', '|': 'z'}
result = ""
for letter in secret:
    #for key, value in clues.items():
#        if value in clues.items():
#    print(key)
    if letter in clues.keys():
        result += clues[letter]
    else:
        result += letter

print(result)
