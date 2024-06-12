import json

from django.test import TestCase

from abampdb.management.commands.load_csv import Command
from abampdb.models import Proteins


class Test(TestCase):
    def test_import(self):
        command = Command()
        expected = {
            "name": "Aurein 1.2",
            "sequence": "GLFDIIKKIAESF",
            "hydrolitic_activity": 0.779,
            "mic_value": 16.0,
            "solubility": "SOLUBLE=0.8",
            "tiny": 3,
            "small": 4,
            "aliphatic": 5,
            "aromatic": 2,
            "non_polar": 8,
            "polar": 5,
            "charged_aa": 4,
            "basic": 2,
            "acidic": 2.0,
            "mol_weight_tiny": 23.077,
            "mol_weight_small": 30.769,
            "mol_weight_apliphatic": 38.462,
            "mol_weight_aromatic": 15.385,
            "mol_weight_non_polar": 61.538,
            "mol_weight_polar": 38.462,
            "mol_weight_charged": 30.769,
            "mol_weight_basic": 15.385,
            "mol_weight_acidic": 15.385,
            "molecular_weight": 1480.767,
            "length": 13,
            "charge": -0.000384161,
            "p_i": 6.492972,
            "a_index": 127.69231,
            "instaIndex": 20.4769231,
            "BomanIndex": 0.1261538,
            "hydrophobicity": 0.6692308,
            "hmoment_angle": 0.7127588,
            "transmembrane": 1,
            "extracellular": True,
            "cytoplasmic": False,
            "hydrophobic_plots": -4.736988417,
            "hydropathy_plots": 1.889359073,
            "disulfide_end": "Leu 2 > Ser 12 ",
            "toxicity": "Non-Toxin",
            "rmsf": 2.68,
            "flexibility": 0.99,
            "pdb_name": "AbAMP1.pdb",
            "links": "http://biocomp.chem.uw.edu.pl/CABSflex2/job/e4fe5a24a0906e9/",  # noqa
        }
        expected["cytoplasmic"] = eval(str(expected["cytoplasmic"]).title())
        # expected['extracellular'] = expected['extracellular'].upper()
        command.handle(csv_dir="ampdb-Final.csv")
        # command.handle(csv_dir='abampdb/static/data.csv')
        self.maxDiff = None
        protein = Proteins.objects.all()[0]
        actual = protein.__dict__
        del actual["_state"]
        del actual["id"]
        self.assertEqual(expected, actual)
