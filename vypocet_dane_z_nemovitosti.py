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
# - forrest (les) má koeficient 0.35,
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
    elif self.estate_type == "forrest":
      tax = (self.area * 0.35 * self.locality.locality_coefficient)
    elif self.estate_type == "garden":
      tax = (self.area * 2 * self.locality.locality_coefficient)
    else:
      return "Chyba: Neplatný typ pozemku. Zadejte: land, building_site, forrest nebo garden."
    
    return ceil(tax)

# Uvažujme tedy například lesní pozemek o ploše 500 metrů čtverečních v lokalitě s místním koeficientem 2. Potom je daň 500 * 0.35 * 2 = 350.


zemedelsky_pozemek1 = Estate(locality_1, "forrest", 500)
print(zemedelsky_pozemek1.calculate_tax())  # Mělo by vrátit 350

zemedelsky_pozemek2 = Estate(locality_3, "building_site", 25)
print(zemedelsky_pozemek2.calculate_tax()) # Mělo by vrátit 788

