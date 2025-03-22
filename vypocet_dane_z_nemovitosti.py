from math import ceil


# V rámci aplikace nejprve vytvoř třídu Locality, která označuje lokalitu, kde se nemovitost nachází. Třída bude mít atributy name (název katastru/obce) a locality_coefficient (tzv. místní koeficient, který se používá k výpočtu daně).

class Locality:
  def __init__(self, name, locality_coefficient):
    self.name = name
    self.locality_coefficient = locality_coefficient

locality_1 = Locality("Ostrava", 2)
locality_2 = Locality("Olomouc", 3)
locality_3 = Locality("Opava", 3.5)

# Vytvoř třídu Property, která bude reprezentovat nějakou nemovitost. Třída bude mít atribut locality (lokalita, kde se pozemek nachází, bude to objekt třídy Locality).

class Property:
  def __init__(self, locality: Locality): 
    self.locality = locality

# Dále vytvoř třídu Estate, která reprezentuje pozemek a je potomkem třídy Property. Třída bude mít atributy locality, estate_type (typ pozemku), area (plocha pozemku v metrech čtverečních). Dále přidej metodu calculate_tax(), která spočítá výši daně pro pozemek a vrátí hodnotu jak celé číslo (pro zaokrouhlení použij funkci ceil() z modulu math). Daň vypočítej pomocí vzorce: plocha pozemku * koeficient dle typu pozemku (atribut estate_type) * místní koeficient. U atributu estate_type následující hodnoty a koeficienty:

# - land (zemědělský pozemek) má koeficient 0.85.
# - building site (stavební pozemek) má koeficient 9.
# - forest (les) má koeficient 0.35,
# - garden (zahrada) má koeficient 2.      


class Estate(Property):
  def __init__(self, locality: Locality, estate_type, area):
    super().__init__(locality)
    self.estate_type = estate_type
    self.area = area

  def calculate_tax(self):
    if self.estate_type == "land":
      tax = (self.area * 0.85 * self.locality.locality_coefficient)
    elif self.estate_type == "building_site":
      tax = (self.area * 9 * self.locality.locality_coefficient)
    elif self.estate_type == "forest":
      tax = (self.area * 0.35 * self.locality.locality_coefficient)
    elif self.estate_type == "garden":
      tax = (self.area * 2 * self.locality.locality_coefficient)
    else:
      return "Chyba: Neplatný typ pozemku. Zadejte: land, building_site, forest nebo garden."
    
    return ceil(tax)

# Uvažujme tedy například lesní pozemek o ploše 500 metrů čtverečních v lokalitě s místním koeficientem 2. Potom je daň 500 * 0.35 * 2 = 350.


zemedelsky_pozemek1 = Estate(locality_1, "forest", 500)
print(zemedelsky_pozemek1.calculate_tax(), " Kč je daň za zemědělský pozemek č. 1.")  # Mělo by vrátit 350

stavebni_pozemek2 = Estate(locality_3, "building_site", 25)
print(stavebni_pozemek2.calculate_tax()) # Mělo by vrátit 788



# Vytvoř třídu Residence`, která reprezentuje byt, dům či jinou stavbu a je potomkem třídy Property. Třída bude mít atributy locality, area (podlahová plocha bytu nebo domu) a commercial (pravdivostní hodnota, která určuje, zda se jedná o nemovitost používanou k podnikání). Dále přidej metodu calculate_tax(), která spočítá výši daně pro byt a vrátí hodnotu jako číslo. Daň vypočítej pomocí vzorce: podlahová plocha * koeficient lokality * 15. Pokud je hodnota parametru commercial True, tj. pokud jde o komerční nemovitost, vynásob celou daň číslem 2.

class Residence(Property):
  def __init__(self, locality: Locality, area, commercial):
    super().__init__(locality)
    self.area = area
    self.commercial = commercial

  def calculate_tax(self):
    if self.commercial == True:
      tax = self.area * self.locality.locality_coefficient * 15 * 2
    elif self.commercial == False:
      tax = self.area * self.locality.locality_coefficient * 15 
    else:
      return ("Parametr commercial musí být true nebo false.")
    
    return ceil(tax)
  
# Příklad výpočtu: Uvažujme tedy například byt (určený k bydlení) o ploše 60 metrů čtverečních v lokalitě s koeficientem 3. Potom je daň 60 * 3 * 15 = 2700. Pokud by stejný byt byl používán k podnikání, daň by byla 60 * 3 * 15 * 2 = 5400.

byt1 = Residence(locality_2, 60, False)
byt2 = Residence(locality_2, 60, True)

print(byt1.calculate_tax()) # očekávaný výstup: 2700
print(byt2.calculate_tax()) # očekávaný výstup: 5400


# Vyzkoušej svůj program pomocí následujících nemovitostí:

# - Zemědělský pozemek o ploše 900 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 900 * 0.85 * 0.8 = 612.

locality_4 = Locality("Manětín", 0.8)
zemedelsky_pozemek3 = Estate(locality_4, "land", 900)
print(zemedelsky_pozemek3.calculate_tax()) # Mělo by vrátit 612


# - Dům s podlahovou plochou 120 metrů čtverečních v lokalitě Manětín s koeficientem 0.8. Daň z této nemovitosti je 120 * 0.8 * 15 = 1440.

rodinny_dum = Residence(locality_4, 120, False)
print(rodinny_dum.calculate_tax()) # očekávaný výstup: 1440


# - Kancelář (tj. komerční nemovitost) s podlahovou plochou 90 metrů čtverečních v lokalitě Brno s koeficientem 3. Daň z této nemovitosti je 90 * 3 * 15 * 2 = 8100.

locality_5 = Locality("Brno", 3)
kancelar = Residence(locality_5, 90, True)
print(kancelar.calculate_tax()) # očekávaný výstup: 8100
