from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="create group", header="create logo", footer="create comment"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
