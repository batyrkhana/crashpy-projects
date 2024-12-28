url = "https://pokemon.gov"
url1 = url.removeprefix("https://")
url2 = url.removesuffix(".gov")
url3 = url.removeprefix("https://").removesuffix(".gov")
print(f"Modified urls:\n\t{url1}\n\t{url2}\n\t{url3}")