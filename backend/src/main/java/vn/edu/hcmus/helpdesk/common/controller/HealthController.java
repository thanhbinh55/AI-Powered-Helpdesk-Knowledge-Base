package vn.edu.hcmus.helpdesk.common.controller;

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

    private final DataSource dataSource;

    public HealthController(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @GetMapping("/health")
    public ResponseEntity<ApiResponse<Map<String, Object>>> checkHealth() {
        Map<String, Object> status = new LinkedHashMap<>();
        status.put("status", "UP");
        status.put("service", "helpdesk-backend");
        status.put("version", "0.0.1-SNAPSHOT");

        try (Connection conn = dataSource.getConnection()) {
            status.put("database", "CONNECTED");
            status.put("db_metadata", conn.getMetaData().getDatabaseProductName() + " " + conn.getMetaData().getDatabaseProductVersion());
        } catch (Exception e) {
            status.put("database", "DOWN");
            status.put("database_error", e.getMessage());
        }

        return ResponseEntity.ok(ApiResponse.of(status));
    }
}
