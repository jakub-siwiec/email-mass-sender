class Templatescontainer:
    def __init__(self, general_template, personal_template):
        """Container class for types of templates. There are 2 types: general (when the recipient is unknown) and personal (when we address an email to the specific person)

        Args:
            general_template (template object): Template for an unknown recipient
            personal_template ([type]): Template for a known recipient
        """
        self.personal_template = personal_template
        self.general_template = general_template

    def personal(self):
        """ Get personal template

        Returns:
            template object: Personal template object
        """
        return self.personal_template

    def general(self):
        """ Get general template

        Returns:
            template object: General template object
        """

        return self.general_template
