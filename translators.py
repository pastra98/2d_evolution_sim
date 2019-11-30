from body import ShapeTranscriptor
from movement import ThrusterTranscriptor

# Transcriptors are responsible for performing the instructions of genes
# and temporarily storing relevant data described in genes.

class Transcriptor:
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
        self.transcription_data = {}
        self.rna = genes_to_express # genes to be expressed
        self.shape_transcriptor = ShapeTranscriptor()
        self.thruster_transcriptor = ThrusterTranscriptor()
        self.sub_transcriptors = [self.shape_transcriptor,
                                  self.thruster_transcriptor]

    def express_genome(self):
        """hands the dict of expressed genes to the specialized
        sub-ranscriptors. Then returns the updated transcription_data
        dictionary filled with all data decoded by the subtranscriptors.
        """
        while len(self.sub_transcriptors) > 0:
            for sub_t in self.sub_transcriptors:
                t_data = sub_t.run(self.rna, self.transcription_data)
                if t_data == None:
                    pass
                else:
                    self.transcription_data.update(t_data)
                    self.sub_transcriptors.remove(sub_t)

        return self.transcription_data


