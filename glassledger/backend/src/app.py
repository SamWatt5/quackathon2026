from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import firebase_admin
from firebase_admin import credentials, firestore as fs


cred = credentials.Certificate("service-account.json")
firebase_admin.initialize_app(cred)
firebase_db = fs.client()

app = Flask(__name__)
CORS(app)

DB = "glass_ledger.db"


def query(sql, params=()):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    rows = con.execute(sql, params).fetchall()
    con.close()
    return [dict(r) for r in rows]


@app.get("/api/person/<int:id>")
def get_person(id):
    people = query("SELECT * FROM people WHERE id = ?", (id,))
    if not people:
        return jsonify({"error": "not found"}), 404
    person = people[0]
    person["transactions"] = query(
        "SELECT * FROM transactions WHERE person_id = ? ORDER BY date DESC",
        (id,)
    )
    person["flags"] = query(
        "SELECT * FROM flags WHERE person_id = ?",
        (id,)
    )
    return jsonify(person)


@app.get("/api/resolve")
def resolve():
    name = request.args.get("name", "").lower()
    people = query("SELECT id, name, role FROM people")
    for p in people:
        if name in p["name"].lower():
            return jsonify(p)
    return jsonify({"error": "no match"}), 404


@app.get("/api/explore")
def explore():
    return jsonify(query(
        "SELECT id, name, role, party, transparency_score FROM people"
    ))


@app.get("/api/watchlist")
def watchlist():
    ids = request.args.get("ids", "")
    if not ids:
        return jsonify([])
    id_list = [int(i) for i in ids.split(",")]
    placeholders = ",".join("?" * len(id_list))
    return jsonify(query(
        f"SELECT id, name, role, party, transparency_score FROM people WHERE id IN ({placeholders})",
        id_list
    ))


@app.get("/api/subscriptions/<uid>")
def get_subscriptions(uid):
    docs = firebase_db.collection("users").document(
        uid).collection("subscriptions").stream()
    ids = [int(doc.to_dict()["personId"]) for doc in docs]
    return jsonify(ids)


if __name__ == "__main__":
    app.run(debug=True)
