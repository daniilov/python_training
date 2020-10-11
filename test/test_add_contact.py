from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="t",
                               company="c",
                               address="a", homenumber="1", mobilenumber="2", worknumber="3", faxnumber="4",
                               email1="m1",
                               email2="m2", email3="m3", homepage="h", address2="sa",
                               home2="sh", notes="sn"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", homenumber="", mobilenumber="", worknumber="", faxnumber="",
                               email1="",
                               email2="", email3="", homepage="", address2="",
                               home2="", notes=""))
    app.session.logout()
