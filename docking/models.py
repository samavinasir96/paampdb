from django.db import models


class TargetProtein(models.Model):
    target_protein = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.target_protein

class AMP(models.Model):
    target_protein = models.ForeignKey(TargetProtein, on_delete=models.SET_NULL, null=True, blank=True)
    amp_no = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    sequence = models.TextField()
    source = models.CharField(max_length=255)
    tiny_number = models.IntegerField()
    small_number = models.IntegerField()
    aliphatic_number = models.IntegerField()
    aromatic_number = models.IntegerField()
    nonpolar_number = models.IntegerField()
    polar_number = models.IntegerField()
    charged_number = models.IntegerField()
    basic_number = models.IntegerField()
    acidic_number = models.IntegerField()
    tiny_mole = models.FloatField()
    small_mole = models.FloatField()
    aliphatic_mole = models.FloatField()
    aromatic_mole = models.FloatField()
    nonpolar_mole = models.FloatField()
    polar_mole = models.FloatField()
    charged_mole = models.FloatField()
    basic_mole = models.FloatField()
    acidic_mole = models.FloatField()
    molecular_weight = models.CharField(max_length=50)
    length = models.IntegerField()
    isoelectric_point = models.CharField(max_length=50)
    aliphatic_index = models.FloatField()
    antigenic = models.CharField(max_length=255)
    toxicity = models.CharField(max_length=255)
    cpp = models.CharField(max_length=255)
    charge = models.CharField(max_length=50)
    instability_index = models.CharField(max_length=50)
    hydrophobicity = models.CharField(max_length=50)
    hydrophobic_moment = models.CharField(max_length=50)
    boman_index = models.CharField(max_length=50)
    hp = models.CharField(max_length=50)
    antimicrobial = models.CharField(max_length=255)
    half_life = models.CharField(max_length=255)
    pdb_name = models.CharField(("PDBName"), max_length=1000)
    pdb_file = models.FileField(upload_to='amp_pdb_files/', null=True, blank=True)

    def __str__(self):
        return self.name

class Dock(models.Model):
    amp = models.ForeignKey(AMP, on_delete=models.CASCADE)
    target_protein = models.ForeignKey(TargetProtein, on_delete=models.CASCADE)
    dock = models.CharField(max_length=255)
    pdb_structure = models.FileField(upload_to='dock_pdb_files/', null=True, blank=True)
    pdb_structure_name = models.CharField(max_length=1000)
    avg_rmsd = models.CharField(max_length=50)
    lowest_rmsd = models.CharField(max_length=50)
    binding_energy = models.CharField(max_length=50)
    ligplot = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.amp} - {self.target_protein} - {self.dock}"
    

class PDBQuery(models.Model):
    query_id = models.CharField(max_length=1000)
    # email = models.CharField(max_length=200)

    def __str__(self):
        return self.query_id

class PDBTQuery(models.Model):
    query_id = models.CharField(max_length=1000)
    # email = models.CharField(max_length=200)

    def __str__(self):
        return self.query_id

class PDBDQuery(models.Model):
    query_id = models.CharField(max_length=1000)
    # email = models.CharField(max_length=200)

    def __str__(self):
        return self.query_id