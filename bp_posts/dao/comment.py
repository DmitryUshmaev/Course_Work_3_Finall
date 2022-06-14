class Comment:

    def __init__(self, post_id=0, commenter_name="", comment="", pk=0):
        self.post_id = post_id
        self.comment = comment
        self.commenter_name = commenter_name
        self.pk = pk

    def __repr__(self):

        return f"Commen("\
        f"{self.pk}),"\
        f"{self.comment}),"\
        f"{self.commenter_name}),"\
        f"{self.post_id}),"\
        f")"
