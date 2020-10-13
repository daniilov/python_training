from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="t",
                               company="c", address="a", home="1", mobile="2", work="3", fax="4", email="m1",
                               email2="m2", email3="m3", homepage="h", address2="sa", phone2="sh", notes="sn"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", home="", mobile="", work="", fax="", email="", email2="", email3="",
                               homepage="", address2="", phone2="", notes=""))
    app.session.logout()
