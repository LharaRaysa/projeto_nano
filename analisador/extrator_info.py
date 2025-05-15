import re

class NanoAnalyzer:
    def __init__(self):
        self.nanoparticle_keywords = ['nanoparticle', 'nanoparticles', 'TiO2', 'titania', 'graphene', 'silver', 'gold', 'carbon', 'quantum dot']
        self.utility_keywords = ['coating', 'sensor', 'optical', 'photovoltaic', 'catalysis', 'biomedical', 'light-emitting', 'encapsulant']
        self.fabrication_keywords = ['ASPD', 'spray', 'plasma', 'sol-gel', 'UV curing', 'vapor phase', 'spin-coating', 'thermal']
        self.polymer_keywords = ['polymer', 'polystyrene', 'PMMA', 'polyimide', 'polycarbonate', 'epoxy', '4-bromostyrene']
        self.application_keywords = ['LED', 'lens', 'solar', 'waveguide', 'optical fiber', 'photodetector']

    def analisar(self, texto):
        def buscar(lista): return re.findall(r'\b(?:' + '|'.join(lista) + r')\b', texto, re.IGNORECASE)
        np = buscar(self.nanoparticle_keywords)
        utils = buscar(self.utility_keywords)
        fabric = buscar(self.fabrication_keywords)
        polymer = buscar(self.polymer_keywords)
        apps = buscar(self.application_keywords)
        size = re.findall(r'(\d{1,3}\s?(?:nm|nanometers))', texto)
        patents = re.findall(r'(?:US|WO|EP)\s?\d+[\-/]?\d*', texto)
        if not patents and "patent" in texto.lower():
            patents = ["Mencionada, mas não especificada"]

        return {
            "nanopartículas": ', '.join(set(np)) or "Não identificadas",
            "utilidades": ', '.join(set(utils)) or "Não identificadas",
            "patentes": ', '.join(set(patents)) or "Nenhuma",
            "tamanho": ', '.join(set(size)) or "Não informado",
            "técnica": ', '.join(set(fabric)) or "Não identificada",
            "composição": ', '.join(set(polymer)) or "Não identificada",
            "aplicações": ', '.join(set(apps)) or "Não mencionadas",
            "np_count": len(set(np)),
            "app_count": len(set(apps)),
            "tech_count": len(set(fabric))
        }
