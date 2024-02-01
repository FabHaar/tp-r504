import java.io.* ;
import java.net.* ;
import javax.json.* ;	
import java.util.Scanner;

import org.apache.http.HttpEntity;
import org.apache.http.client.*;
import org.apache.http.client.methods.*;
import org.apache.http.impl.client.*;


//pour faire fonctionner le programme utiliser une URL de ce type depuis le site https://omdbapi.com/
//www.omdbapi.com/?APIKEY="$apikey"&t=mario
//pour tester : ./run.sh Client2 "www.omdbapi.com/?APIKEY=751ea6aa&t=oppenheimer"
public class Client3
{
	public static void main(String[] args)
	{
		try {
	//definir la variable titre en entrée, événement interact user, entrée while
	//tester si titre rentrée ou la valeur d'arret
	//faire valeur arret while

			// code a executer
			CloseableHttpClient client = HttpClients.createDefault();
			//lancement du while
			String entree = "1";
			while ( !entree.equals("0")) {
				
				//récupération d'entrée utilisateur
				Scanner sc = new Scanner(System.in);
				System.out.println("Veuillez saisir un titre de film :");
				String titre = sc.nextLine();
				System.out.println("Vous rechercher le titre : " + titre);
				


				
				//appplication du titre récupérer dans une URL
				String url = "http://" + "www.omdbapi.com/?APIKEY=751ea6aa&t=" + titre ;
				HttpGet request = new HttpGet(url);
				
				
				//requête
				System.out.println( "Executing request " + request.getRequestLine() );
				
				
				
				//réponse et information du status de la réponse :
				CloseableHttpResponse resp = client.execute(request);
				
				System.out.println( "Response Line: " + resp.getStatusLine() );
				System.out.println( "Response Code: " + resp.getStatusLine().getStatusCode() );
			
			
			
			
			
				//récuperation du JSON (parser) et exploitation
				InputStreamReader isr = new InputStreamReader( resp.getEntity().getContent() );	
				//lecture du JSON
				JsonReader reader = Json.createReader(isr);
				JsonObject jsonObject = reader.readObject();
				
				System.out.println( "Date de sortie : " + jsonObject.getString("Released") );
				System.out.println( "Acteurs principaux : " + jsonObject.getString("Actors") );
				System.out.println( "Durée : " + jsonObject.getString("Runtime") );
				
				String rtavis = "";
				JsonArray tab = jsonObject.getJsonArray("Ratings");
				for( int i=0; i<tab.size(); i++ ) {
					JsonObject ji = tab.getJsonObject(i);
					if ("Rotten Tomatoes".equals(ji.getString("Source"))) {
						rtavis = ji.getString("Value");
						System.out.println("Avis : " + rtavis);
					}
				
				}
				// Retirer le pourcentage de la chaîne
				String nombreStr = rtavis.replaceAll("[^0-9]", "");

				// Convertir la chaîne en entier
				int avis = Integer.parseInt(nombreStr);
				if ( avis < 20){
					System.out.println("Nul");
				}
				else if ( avis < 50) {
					System.out.println("Bof");
				}
				else if ( avis < 70) {
					System.out.println("Bien");
				}
				else {
					System.out.println("Très bien");
				}
				
				//fermeture d'exploitation du JSON
				reader.close();
				isr.close();
				
				//sortie ou continuation while
				Scanner input = new Scanner(System.in);
				System.out.println("Pour arreter veuillez saisir 0 sinon rien : ");
				entree = input.nextLine();
				
	
			}
				
		}
		catch( Exception ex ) {
			System . out . println( " erreur ! " ) ;
			//ex . printStackTrace ( ) ;
		}
	}
}
