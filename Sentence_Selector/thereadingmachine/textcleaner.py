def textcleaner(text):
    dic = {"\r" : " ",
           "         You must be                       You must be  I leave a flower here:      Efficacit et Transparence des Acteurs Europens   1999-2016." : " ",
           "Efficacit et Transparence des Acteurs Europens" : " ",
           "            EurActiv.com             " : " ",
           "/* customize styles to your web-site */ .mp_releases_box {  border: solid #999999 1px;  background-color: #FFFFFF; } #mp_releases {  font-family:Geneva, Arial, Helvetica, sans-serif;  padding-top: 0px;  position: relative;  vertical-align: bottom; } #mp_releases li {  margin-top: 3px; } #mp_releases a {  color: #0033CC;  font-size: 12px;  text-decoration: underline; } #mp_releases a:hover {  color: #CC0000;  font-size: 12px; } .ferthead {  font-size: 14px;  color: #000000; } .fertheadbox {  padding-left: 10px;  padding-top: 10px; }" : " ",
           "/*" : " ",
           "customize styles to your web-site" : " ",
           " .mp_releases_box " : " ",
           "border: solid" : " ",
           "background-color:" : " ",
           "#FFFFFF;" : " ",
           "#mp_releases" : " ",
           "font-family:Geneva" : " ",
           "Arial" : " ",
           "Helvetica" : " ",
           "sans-serif" : " ",
           "padding-top:" : " ",
           "0px" : " ",
           "1px" : " ",
           "position: relative" : " ",
           "vertical-align" : " ",
           "margin-top" : " ",
           "3px" : " ",
           "color:" : " ",
           "#0033CC" : " ",
           "12px" : " ",
           "font-size" : " ",
           "text-decoration" : " ",
           "#CC0000" : " ",
           ".ferthead" : " ",
           "14px" : " ",
           "#000000" : " ",
           ".fertheadbox" : " ",
           "padding-left:" : " ",
           "10px" : " ",
           "padding-top:" : " ",
           "   " : " ",
           "#999999" : " ",
           "background-" : " ",
           "a:hover" : " ",
           "}  box {" : " ",
           "underline;" : " ",
           "bottom;" : " ",
           "//" : " ",
           "}   {" : " ",
           "} li {" : " ",
           "} a {" : " ",
           "} {" : " ",
           ",  ," : " ",
           ",  ;" : " ",
           "   ;" : " ",
           "; :" : " ",
           "               " : " ",
           "\\" : " "
           }
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text