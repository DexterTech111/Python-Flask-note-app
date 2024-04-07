from website import create_app

app = create_app()

if __name__ == '__main__': #this below code should execute only if we run this file as the main script and not when we import the this file another file
    app.run(debug=True) #any time a code is changes, automatically run the webserver