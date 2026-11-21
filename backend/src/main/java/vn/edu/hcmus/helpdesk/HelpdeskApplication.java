package vn.edu.hcmus.helpdesk;

import io.github.cdimascio.dotenv.Dotenv;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.File;

@SpringBootApplication
public class HelpdeskApplication {

    public static void main(String[] args) {
        loadDotenv();
        SpringApplication.run(HelpdeskApplication.class, args);
    }

    private static void loadDotenv() {
        try {
            File envFile = new File("../.env");
            String dir = envFile.exists() ? ".." : ".";
            Dotenv dotenv = Dotenv.configure().directory(dir).ignoreIfMissing().load();
            dotenv.entries().forEach(entry -> {
                if (System.getProperty(entry.getKey()) == null) {
                    System.setProperty(entry.getKey(), entry.getValue());
                }
            });
        } catch (Exception ignored) {
        }
    }
}

