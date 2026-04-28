from service.disco_service import DiscoService
from model.artist import Artist
from model.album import Album


class DiscoController:

    def getArtists(self):
        service = DiscoService()
        artisti = service.getAllArtist()
        output = []

        for artista in artisti:
            temp = Artist(artista.get("ArtistId", 0), artista.get("Name", "Artista aconosciuto"))
            output.append(temp.toTuple())
        return output


    def getArtistiJson(self):
        service = DiscoService()
        return service.getAllArtist()



