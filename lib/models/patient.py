class Patient:
     def __init__(self, name, illness, insurance):
          if not isinstance(name, str) or not len(name) > 0:
               raise AttributeError("Name must be a string longer than 0 characters.")
          self.name = name

          if not isinstance(illness, str) or not (0 > len(illness) > 20):
               raise AttributeError("Illness must be a string between 0 and 20 characters.")
          self.illness = illness

          if not isinstance(insurance, str) or insurance not in ("Y", "N"):
               raise AttributeError("Insurance must be either 'Y' or 'N'")
          self.insurance = insurance

