package vn.edu.hcmus.helpdesk.common.api;

import java.util.List;

public record PageResponse<T>(List<T> data, PageMetadata page) {
    public record PageMetadata(int number, int size, long totalElements, int totalPages) {}

    public static <T> PageResponse<T> of(List<T> data, int number, int size, long totalElements, int totalPages) {
        return new PageResponse<>(data, new PageMetadata(number, size, totalElements, totalPages));
    }
}
