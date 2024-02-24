from website import create_app

app = create_app()

if __name__ == '__main__':
    # Remember to set debug=False when running application in deployment environment
    app.run(host='0.0.0.0', port=5000, debug=True)