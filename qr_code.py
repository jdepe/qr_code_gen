import segno
from segno import helpers

test_1 = segno.make("Test")
test_1.save("Test.png", scale = 30, border = 5)

test_2 = segno.make("Testing")
test_2.save("Test2.png", scale = 30, border = 5, dark = "#0041f5", data_dark = "yellow", light = "#00dcf5")

# Test with details
test_with_details = helpers.make_mecard(name = "Jaden", email = "jaden.dep@gmail.com", url = "https://www.linkedin.com/in/jaden-de-penning/")

test_with_details.designator
'3-L'

test_with_details.save("contact.png", scale = 5, border = 5, dark = "darkred", data_dark = "darkorange", light = "yellow")






