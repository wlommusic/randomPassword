from flask import Flask, request

from hash import do_md5

app = Flask(__name__)
app.static_folder = 'static'

app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        string = None

        try:
            string = float,str(request.form["string"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["string"])

        if string is not None:
            result = do_md5(string)
            return '''
                <html>
                <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width; initial-scale=1.0;">
                </head>
                <body  styles="color:yellow;">
                        <p styles="color:yellow;">The result is </p>
                        <p> {result} </p>
                        <p style="styles="color:yellow;"><a href="/">Click here to Generate again</a>
                    </body>
             <footer style=" font-family: Arial,Helvetica,sans-serif;color:red;box-sizing: border-box; position:absolute;bottom:0;height:90px;width: 100%; text-align: background-color: #000000;border-top: 1.75px solid red;padding: 0";>
            Author : Dipta ranjan Panda &copy;
            <div style="font-family: Arial,Helvetica,sans-serif;font-weight: bold;"> Made using Flask</div>
            <div>
            <a href="https://discord.gg/NarJukR7zB" target="_blank"> <img border="0" alt="Discord" src="https://www.freepnglogos.com/uploads/discord-logo-png/discord-logo-logodownload-download-logotipos-1.png" width="50" height="50"> </a>
            <a href="https://github.com/wlommusic" target="_blank"> <img border="0" alt="Github" src="https://image.flaticon.com/icons/png/512/25/25231.png" width="50" height="50"> </a>
            <a href="https://spotify.com/artist/3VAsl4hVBSwi1Z2Ysb9kuf?si=4OvHUvs8TIurj3mdp2Mk3g" target="_blank"> <img border="0" alt="spotify" src="https://www.freeiconspng.com/uploads/spotify-icon-2.png" width="50" height="50"> </a>
            </div>
            </footer>
                </html>
            '''.format(result=result)

    return '''
       <html>
        <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width; initial-scale=1.0;">
        <title >Random password generator
        </title>
        <meta name="viewport" content="width=device-width; initial-scale=1.0;">
        <link rel="stylesheet" type="text/css" href="https://www.pythonanywhere.com/user/diptapanda/files/home/diptapanda/mysite/static/styles.css" media="screen"/>
        <link rel="icon" href="https://library.kissclipart.com/20181208/qqw/kissclipart-cyber-security-lock-png-clipart-computer-security-e5885498dc62118e.jpg" type="image/icon type">


        </head>

            <body style="text-align: center; font-family: Arial,Helvetica,sans-serif;background-color: #000000;
background-color: #2d3436;
background-image: linear-gradient(315deg, #2d3436 0%, #000000 74%);;color: white;
background-repeat: no-repeat; margin: 0;box-sizing: border-box;height: 100%">

                <h1 style=" text-transform: uppercase; background: linear-gradient(to right, #c6bfd0 0%, #5d15c5 105%);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;font-style: italic;">RANDOM PASSWORD GENERATOR</h1>
                <h2 style="color:pink;font-s ">Use this generator to create a 16 digit secure random password from a string:</h2>
                <p> Enter any string or your old password and this app will randomize a new secure password for you using our advanced algorithm.</p>
                <form  method="post" action=".">
                    <p><input name="string" /></p>
                    <p ><input type="submit" value="GENERATE" /></p>
                </form>
                <p style=" border:1px solid black;width:90%;height:150px;margin-right:auto;margin-left:auto;
               color:yellow;text-transform: uppercase;font-size: larger;font-style: italic;">
                    Strong passwords are utterly important – they prevent unauthorized access to your electronic accounts and devices.
                    If you choose a very complicated and long password, you will make it very difficult for a hacker to crack it, whether by a brute-force attack (i.e., trying every possible combination of numbers, letters or special characters) or an automated machine attack trying thousands of combinations per second to guess your one and only.
                    So, the more complex your password is, the more security it provides for your account. Remember that your account is where you store a great deal of sensitive information that you don’t want to have stolen. As you understand, the stakes are very high. Therefore, taking care of your account password is crucial.
            </p>
            </body>

            <footer style=" font-family: Arial,Helvetica,sans-serif;color:red;box-sizing: border-box; position:absolute;bottom:0;height:90px;width: 100%; text-align: background-color: #000000;
background-image: linear-gradient(147deg, #000000 0%, #434343 74%);border-top: 1.75px solid red;padding: 0";>
            Author : Dipta ranjan Panda &copy;
            <div style="font-family: Arial,Helvetica,sans-serif;font-weight: bold;"> Made using Flask</div>
            <div>
            <a href="https://discord.gg/NarJukR7zB" target="_blank"> <img border="0" alt="Discord" src="https://www.freepnglogos.com/uploads/discord-logo-png/discord-logo-logodownload-download-logotipos-1.png" width="50" height="50"> </a>
            <a href="https://github.com/wlommusic" target="_blank"> <img border="0" alt="Github" src="https://image.flaticon.com/icons/png/512/25/25231.png" width="50" height="50"> </a>
            <a href="https://spotify.com/artist/3VAsl4hVBSwi1Z2Ysb9kuf?si=4OvHUvs8TIurj3mdp2Mk3g" target="_blank"> <img border="0" alt="spotify" src="https://www.freeiconspng.com/uploads/spotify-icon-2.png" width="50" height="50"> </a>
            </div>
            </footer>
        </html>


    '''.format(errors=errors)