package vn.edu.hcmus.helpdesk.common.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import vn.edu.hcmus.helpdesk.common.api.ApiResponse;

import javax.sql.DataSource;
import java.sql.Connection;
import java.util.LinkedHashMap;
import java.util.Map;

@RestController
@RequestMapping("/api/v1")
public class HealthController {

    private static final Logger log = LoggerFactory.getLogger(HealthController.class);
    private final DataSource dataSource;

    public HealthController(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @GetMapping("/health")
    public ResponseEntity<ApiResponse<Map<String, Object>>> checkHealth() {
        Map<String, Object> status = new LinkedHashMap<>();
        status.put("service", "helpdesk-backend");
        status.put("version", "0.0.1-SNAPSHOT");

        try (Connection conn = dataSource.getConnection()) {
            status.put("status", "UP");
            status.put("database", "CONNECTED");
            status.put("db_metadata", conn.getMetaData().getDatabaseProductName() + " " + conn.getMetaData().getDatabaseProductVersion());
            return ResponseEntity.ok(ApiResponse.of(status));
        } catch (Exception e) {
            log.error("Database connection health check failed: {}", e.getMessage(), e);
            status.put("status", "DOWN");
            status.put("database", "DISCONNECTED");
            return ResponseEntity.status(HttpStatus.SERVICE_UNAVAILABLE).body(ApiResponse.of(status));
        }
    }
}

