class BuildMinimumSequenceIdentityString:
    def __call__(self, minimum_sequence_identity: str):
        minimum_sequence_identity = minimum_sequence_identity.replace("%", "")
        minimum_sequence_identity = minimum_sequence_identity.replace(".", "")
        minimum_sequence_identity = "0." + minimum_sequence_identity

        return minimum_sequence_identity
