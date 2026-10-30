from flask import Flask

app = Flask(__name__)

@app.route('/alkuluku/<int:number>')
def alkuluku(number: int):
    if number <= 1:
        prime = False
    else:
        prime = True
        ix = 2
        while ix * ix <= number:
            if number % ix == 0:
                prime = False
                break
            ix += 1


    return {"Number":number, "isPrime":prime}


if __name__ == "__main__":
    app.run(port=3000, debug=True)
