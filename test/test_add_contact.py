import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="t",
                               company="c",
                               address="a", homenumber="1", mobilenumber="2", worknumber="3", faxnumber="4",
                               email1="m1",
                               email2="m2", email3="m3", homepage="h", address2="sa",
                               home2="sh", notes="sn"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                               address="", homenumber="", mobilenumber="", worknumber="", faxnumber="",
                               email1="",
                               email2="", email3="", homepage="", address2="",
                               home2="", notes=""))
    app.logout()
