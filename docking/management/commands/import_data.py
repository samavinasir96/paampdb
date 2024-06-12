import csv
import os
from django.core.management.base import BaseCommand
from docking.models import AMP, TargetProtein, Dock
from django.core.files import File

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.import_amino_acids()
        self.import_target_proteins()
        self.import_docks()

    def import_amino_acids(self):
        with open('D:/ASAB/Maryam_DB/maryam_data/amps.csv', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames
            print(headers)
            for row in reader:
                amp = AMP(
                    amp_no = row['AMP'],
                    name=row['Name'],
                    sequence=row['Sequence'],
                    source=row['Source'],
                    tiny_number=row['Tiny_Number'],
                    small_number=row['Small_Number'],
                    aliphatic_number=row['Aliphatic_Number'],
                    aromatic_number=row['Aromatic_Number'],
                    nonpolar_number=row['NonPolar_Number'],
                    polar_number=row['Polar_Number'],
                    charged_number=row['Charged_Number'],
                    basic_number=row['Basic_Number'],
                    acidic_number=row['Acidic_Number'],
                    tiny_mole=float(row['Tiny_Mole']),
                    small_mole=row['Small_Mole'],
                    aliphatic_mole=row['Aliphatic_Mole'],
                    aromatic_mole=row['Aromatic_Mole'],
                    nonpolar_mole=row['NonPolar_Mole'],
                    polar_mole=row['Polar_Mole'],
                    charged_mole=row['Charged_Mole'],
                    basic_mole=row['Basic_Mole'],
                    acidic_mole=row['Acidic_Mole'],
                    molecular_weight=row['Molecularweight'],
                    length=row['LengthofPeptide'],
                    isoelectric_point=row['isoelectricpoint'],
                    aliphatic_index=float(row['aliphaticindexofprotein']),
                    antigenic=row['antigenic det.'],
                    toxicity=row['toxicity'],
                    cpp=row['CPP'],
                    charge=row['Net Charge'],
                    instability_index=row['instability index'],
                    hydrophobicity=row['Hydrophobicity'],
                    hydrophobic_moment=row['Hydriphobic moment'],
                    boman_index=row['BomanIndex'],
                    hp=row['HP'],
                    antimicrobial=row['anti-microbial'],
                    half_life=row['half life (intestine)'],
                    pdb_name=row['PDBName'],
                )
                
                pdb_file_path = os.path.join('D:/ASAB/Maryam_DB/maryam_data/Anti microbial Peptides', row['PDBName'])
                
                if os.path.exists(pdb_file_path):
                    with open(pdb_file_path, 'rb') as pdb_file:
                        amp.pdb_file.save(row['PDBName'], File(pdb_file), save=False)
                amp.save()

    # def import_target_proteins(self):
    #     with open('D:/ASAB/Maryam_DB/maryam_data/Targets.csv', newline='') as csvfile:
    #         reader = csv.DictReader(csvfile)
    #         for row in reader:
    #             TargetProtein.objects.create(
    #                 target_protein=row['Target Proteins']
    #             )

    def import_target_proteins(self):
        with open('D:/ASAB/Maryam_DB/maryam_data/Targets.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                target_protein = TargetProtein(
                    target_protein=row['Target Proteins'],
                )      
                target_protein.save()

    def import_docks(self):
        with open('D:/ASAB/Maryam_DB/maryam_data/Reshaped_Docking_Results(new).csv', newline='', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                amp = AMP.objects.get(amp_no=row['AMP'].strip())
                target_protein = TargetProtein.objects.get(target_protein=row['Target Proteins'].strip())
                dockcomplexes = Dock(
                    amp=amp,
                    target_protein=target_protein,
                    dock = row['Dock'],
                    pdb_structure=row['pdb_structure'],
                    pdb_structure_name=row['pdb_structure'],
                    avg_rmsd=row['Avg. RMSD'],
                    lowest_rmsd=row['Lowest RMSD'],
                    binding_energy=row['Binding Energy'],
                    ligplot = row['Ligplot'],
                )   
                dock_pdb_files = os.path.join('D:/ASAB/Maryam_DB/maryam_data/Dock_Structures', row['pdb_structure'])
                
                if os.path.exists(dock_pdb_files):
                    with open(dock_pdb_files, 'rb') as pdb_s_file:
                        dockcomplexes.pdb_structure.save(row['pdb_structure'], File(pdb_s_file), save=False)
   
                dockcomplexes.save()

                # Dock.objects.create(
                #     amp=amp,
                #     target_protein=target_protein,
                #     dock = row['Dock'],
                #     pdb_structure=row['pdb_structure'],
                #     avg_rmsd=row['Avg. RMSD'],
                #     lowest_rmsd=row['Lowest RMSD']
                # )
                # dock_pdb_files = os.path.join('D:/ASAB/Maryam_DB/maryam_data/Dock_Structures', row['pdb_structure'])
                
                # if os.path.exists(dock_pdb_files):
                #     with open(dock_pdb_files, 'rb') as pdb_s_file:
                #         amp.pdb_file.save(row['pdb_structure'], File(pdb_s_file), save=False)
                # amp.save()
