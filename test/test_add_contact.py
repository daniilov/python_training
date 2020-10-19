from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fn", middlename="mn", lastname="ln", nickname="nn", title="t",
                      company="c", address="a", home="1", mobile="2", work="3", fax="4", email="m1",
                      email2="m2", email3="m3", homepage="h", address2="sa", phone2="sh", notes="sn")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
