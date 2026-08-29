from flask import Flask, request, make_response, jsonify, render_template, flash, redirect, url_for

from posudba_service import checkout, return_loan_service, renew_loan_service
from knjiga_service import get_knjige, get_book_by_id, add_knjiga
from visualization_service import get_loaned_books_qty_by_author, get_loaned_books_qty, get_renewals_by_author

app = Flask(__name__)

app.secret_key = "dev-secret-key"
@app.route("/")
def home():
    response = get_knjige()
    return render_template('index.html', knjige=response['data'])

@app.route("/visualizations", methods=["GET"])
def visualizations():
    loaned_books_qty_by_author = get_loaned_books_qty_by_author()
    loaned_books_qty = get_loaned_books_qty()
    renewals_by_author = get_renewals_by_author()


    if loaned_books_qty_by_author["status"] == "Success" and loaned_books_qty["status"] == "Success" and renewals_by_author["status"] == "Success":
        chart_data = {
            "loans_by_author": loaned_books_qty_by_author["data"],
            "loans_by_book": loaned_books_qty["data"],
            "renewals_by_author": renewals_by_author["data"]
        }

        return render_template('loan-visualizations.html', chart_data=chart_data)

    return render_template("404.html")


@app.route("/knjige/<int:book_id>", methods=["GET"])
def show_book(book_id):
    response = get_book_by_id(book_id)

    if response["status"] == 'Success':
        print(bool(response['data']['posudba']))
        return render_template('book-show.html', book=response['data']['book'], loan=response['data']['posudba'])

    return render_template("404.html")



@app.route("/knjige", methods=["GET"])
def vrati_knjige():
    response = get_knjige()

    if response["status"] == "Success":
        return make_response(jsonify(response), 200)

    return make_response(jsonify(response), 400)


@app.route("/knjiga", methods=["POST"])
def create_knjiga():
    try:
        json_request = request.json
    except Exception as e:
        response = {"response": str(e)}
        return make_response(jsonify(response), 400)

    response = add_knjiga(json_request)

    if response['status'] == "Success":
        return make_response(jsonify(response), 200)

    return make_response(jsonify(response), 400)


@app.route("/knjige/<int:book_id>/posudba", methods=["POST"])
def create_checkout(book_id):
    # try:
        response = checkout(book_id)

        if response["status"] == "Success":
            flash(response["message"], "success")
        else:
            flash(response["message"], "error")

    # except Exception as e:
    #     flash(str(e))

        return redirect(url_for("show_book", book_id=book_id))


@app.route("/posudba/<int:loan_id>/renew", methods=["POST"])
def renew_loan(loan_id):
    response = renew_loan_service(loan_id)

    flash(response["message"], response["status"])

    return redirect(url_for("show_book", book_id=response["book_id"]))

@app.route("/posudba/<int:loan_id>/return", methods=["POST"])
def return_loan(loan_id):
    response = return_loan_service(loan_id)

    flash(response["message"], response["status"])

    return redirect(url_for("show_book", book_id=response["book_id"]))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True, use_reloader=True)
