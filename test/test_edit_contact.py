from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        Contact(firstname="edit", middlename="first", lastname="contact", nickname="", title="", company="",
                address="", homenumber="", mobilenumber="", worknumber="", faxnumber="", email1="",
                email2="", email3="", homepage="", address2="", home2="", notes=""))
    app.session.logout()
