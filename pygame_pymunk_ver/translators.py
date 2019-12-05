from body import ShapeTranslator
from movement import ThrusterTranslator

# Transcriptors are responsible for performing the instructions of genes
# and temporarily storing relevant data described in genes.

class Translator:
    """This class contains all methods that are required for transcription.
    Somewhat analogous to ribosomes, mRNA, proteins and everything to
    do with gene transcription and expression.
    To-Do : Figure out if updating of transcription_data should happen
    here or in parent classes.
    """
    def __init__(self, genes_to_express):
        """Initializes with a dictionary that contains all genes that
        should be expressed (genes_to_transcribe).
        Returns a second dict that stores all information returned
        by subtranscriptors(parent classes).
        """
        self.translation_data = {}
        self.rna = genes_to_express
        self.shape_translator = ShapeTranslator()
        self.thruster_translator = ThrusterTranslator()
        self.sub_translators = [self.shape_translator,
                                  self.thruster_translator]

    def translate_genome(self):
        """hands the dict of expressed genes to the specialized
        sub-ranscriptors. Then returns the updated transcription_data
        dictionary filled with all data decoded by the subtranscriptors.
        """
        while len(self.sub_translators) > 0:
            for sub_t in self.sub_translators:
                t_data = sub_t.run(self.rna, self.translation_data)
                if t_data == None:
                    pass
                else:
                    self.translation_data.update(t_data)
                    self.sub_translators.remove(sub_t)

        return self.translation_data


